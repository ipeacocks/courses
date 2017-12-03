from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import index
from django.shortcuts import render_to_response
import mock
from payments.models import User
from django.test import RequestFactory


class MainPageTests(TestCase):

    ###############
    #### Setup ####
    ###############

    @classmethod
    def setUpClass(cls):
        request_factory = RequestFactory()
        cls.request = request_factory.get('/')
        cls.request.session = {}

    ##########################
    ##### Testing routes #####
    ##########################

    def test_root_resolves_to_main_view(self):
        main_page = resolve('/')
        self.assertEqual(main_page.func, index)

    def test_returns_appropriate_html_response_code(self):
        resp = index(self.request)
        self.assertEquals(resp.status_code, 200)

    #####################################
    #### Testing templates and views ####
    #####################################

    def test_returns_exact_html(self):
        resp = index(self.request)
        self.assertEquals(
            resp.content,
            render_to_response("index.html").content
        )

    def test_index_handles_logged_in_user(self):
        # Create the user needed for user lookup from index page
        # Note that we are not saving to the database
        user = User(
            name='jj',
            email='j@j.com'
        )

        # Create a session that appears to have a logged in user
        self.request.session = {"user": "1"}

        with mock.patch('main.views.User') as user_mock:

            # Tell the mock what to do when called
            config = {'get.return_value': user}
            user_mock.objects.configure_mock(**config)

            # Run the test
            resp = index(self.request)

            # Ensure we return the state of the session back to normal so
            # we don't affest other tests
            self.request.session = {}

            # Verify it returns the page for the logged in user
            expectedHtml = render_to_response('user.html', {'user': user}).content
            self.assertEquals(
                resp.content,
                expectedHtml
            )
