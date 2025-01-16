import proto.simple_pb2 as simple_pb2
import proto.complex_pb2 as complex_pb2
import proto.enumerations_pb2 as enumerations_pb2

def simple():
    return simple_pb2.Simple(
        id=42,
        is_simple=True,
        name="My name",
        sample_lists=[1, 2, 3]
    )

def complex():
    message = complex_pb2.Complex()
    message.one_dummy.id = 42
    message.one_dummy.name = "My name"
    message.multiple_dummies.add(id=43, name="My name 2")
    message.multiple_dummies.add(id=44, name="My name 3")
    message.multiple_dummies.add(id=45, name="My name 4")
    return message

def enums():
    return enumerations_pb2.Enumeration(
        # eye_color=enumerations_pb2.EYE_COLOR_GREEN
        eye_color=1
    )

if __name__ == '__main__':
    # print(simple())
    # print(complex())
    print(enums())