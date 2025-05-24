// go run main.go -env_name=staging -env_tag=a -app_name=a911-svc -app_version=1.94.5 -s3_bucket_name=my-configs-fetcher -configs_local_path=/

package main

import (
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"regexp"
	"sort"
	"strings"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
	"github.com/hashicorp/go-version"
)

func isValidSemver(version string) bool {
	// Regular expression for semantic versioning
	// {"1.0.0", "2.1.0-beta", "1.2.3-alpha+001", "v1.0.0", "1.0"}
	regex := `^(\d+)\.(\d+)\.(\d+)(?:-([\da-zA-Z-]+(?:\.[\da-zA-Z-]+)*))?(?:\+([\da-zA-Z-]+(?:\.[\da-zA-Z-]+)*))?$`
	r := regexp.MustCompile(regex)
	return r.MatchString(version)
}

func listS3Directories(bucketName string, prefix string) ([]*version.Version, error) {
	// Initialize a session in us-east-1 that the SDK will use to load
	// credentials from the shared credentials file ~/.aws/credentials.
	sess, err := session.NewSession(&aws.Config{
		Region: aws.String("us-east-1"),
	})
	if err != nil {
		log.Fatalf("failed to create session, %v", err)
	}

	// Create an S3 service client.
	svc := s3.New(sess)

	// Set up parameters for the ListObjectsV2 API call
	params := &s3.ListObjectsV2Input{
		Bucket: aws.String(bucketName),
		Prefix: aws.String(prefix),
	}

	result, err := svc.ListObjectsV2(params)

	if err != nil {
		log.Fatalf("unable to list items in bucket %v, %v", bucketName, err)
	}

	var available_configs_versions []string

	for _, item := range result.Contents {
		if strings.Contains(*item.Key, "application.yaml") {
			parts := strings.Split(*item.Key, "/")

			for _, part := range parts {
				// If the part matches the version format (e.g., 1.101.0)
				if isValidSemver(part) && strings.Count(part, ".") == 2 {
					available_configs_versions = append(available_configs_versions, part)
				}
			}
		}
	}
	// fmt.Println(available_configs_versions)
	versions := make([]*version.Version, len(available_configs_versions))
	for i, raw := range available_configs_versions {
		v, _ := version.NewVersion(raw)
		versions[i] = v
	}

	// After this, the versions are properly sorted
	sort.Sort(sort.Reverse(version.Collection(versions)))

	return versions, err
}

func compareVersions(available_configs_versions []*version.Version, arg_version string) *version.Version {
	v_arg, err := version.NewVersion(arg_version)

	if err != nil {
		log.Fatalf("Wrong version format, %v", err)
	}

	var v_final *version.Version
	for _, v_s3 := range available_configs_versions {
		if v_s3.LessThanOrEqual(v_arg) {
			fmt.Printf("%s is less or equal than %s\n", v_s3, v_arg)
			v_final = v_s3
			break
		}
	}

	if v_final == nil {
		fmt.Printf("There is no sufficient version\n")
	}

	return v_final
}

func DownloadConfig(bucketName string, key string, configsLocalPath string) {
	// Initialize a session in us-east-1 that the SDK will use to load
	// credentials from the shared credentials file ~/.aws/credentials.
	sess, err := session.NewSession(&aws.Config{
		Region: aws.String("us-east-1"),
	})
	if err != nil {
		log.Fatalf("failed to create session, %v", err)
	}

	// Create an S3 service client.
	svc := s3.New(sess)

	// Set up parameters for the ListObjectsV2 API call
	params := &s3.GetObjectInput{
		Bucket: aws.String(bucketName),
		Key:    aws.String(key),
	}

	result, err := svc.GetObject(params)
	if err != nil {
		fmt.Println("Error getting object:", err)
		return
	}
	defer result.Body.Close()

	// Create a file to write the downloaded content
	file, err := os.Create(configsLocalPath + "application.yaml")
	if err != nil {
		fmt.Println("Error creating file:", err)
		return
	}
	defer file.Close()

	// Write the content to the file
	_, err = io.Copy(file, result.Body)
	if err != nil {
		fmt.Println("Error copying content to file:", err)
		return
	}

	fmt.Printf("Successfully downloaded %s from %s\n", key, bucketName)
}

func main() {
	envName := flag.String("env_name", "staging", "Environment name")
	envTag := flag.String("env_tag", "a", "Environment tag")
	appName := flag.String("app_name", "a911", "Application name")
	appVersion := flag.String("app_version", "100.100.100.1000.RELEASE", "Application version")
	bucketName := flag.String("s3_bucket_name", "my-configs-fetcher", "S3 bucket where configs live")
	configsLocalPath := flag.String("configs_local_path", "./", "Configs local path")
	flag.Parse()

	// Debug section
	// fmt.Printf("env_name: %s\n", *envName)
	// fmt.Printf("env_tag: %s\n", *envTag)
	// fmt.Printf("app_name: %s\n", *appName)
	// fmt.Printf("app_version: %s\n", *appVersion)
	// fmt.Printf("s3_bucket_name: %s\n", *bucketName)
	// fmt.Printf("configs_local_path: %s\n", *configsLocalPath)

	if !isValidSemver(*appVersion) {
		log.Fatalf("-app-version is not a semver")
	}

	prefix := fmt.Sprintf("%s-%s/%s", *envName, *envTag, *appName)
	// fmt.Println("", prefix)

	// Call the function to list directories
	var available_configs_versions []*version.Version
	available_configs_versions, _ = listS3Directories(*bucketName, prefix)
	fmt.Println(available_configs_versions)
	v_final := compareVersions(available_configs_versions, *appVersion)
	// fmt.Println(v_final)
	// fmt.Printf("%s-%s/%s/%s/application.yaml", *envName, *envTag, *appName, v_final)
	DownloadConfig(*bucketName, fmt.Sprintf("%s-%s/%s/%s/application.yaml", *envName, *envTag, *appName, v_final), *configsLocalPath)
}
