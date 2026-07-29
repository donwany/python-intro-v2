# ENUM - is a collection of named constant values
from enum import Enum

# create your first ENUM
class Status(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    SHIPPED = "shipped"

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class TrafficLight(Enum):
    RED = "Stop"
    YELLOW = "Slow Down"
    GREEN = "Go"

class Color(Enum):
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"

class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    MANAGER = "manager"
    CUSTOMER = "customer"


status = Status.APPROVED.value
status_name = Status.APPROVED.name
day = Day.TUESDAY.value

print(status)
print(status_name)
print(day)
print(Color.RED.value)
print(Color.GREEN.value)

role = Role.USER
if role == Role.ADMIN:
    print("Welcome Admin")
else:
    print("Welcome User")

print("-" * 50)
# USING THE FOR LOOP 
for day in Day:
    print(day.name, day.value)

print("-" * 50)
for role in Role:
    print(role.name, role.value)

print("-" * 50)

class OrderStatus(Enum):
    PENDING = "Pending"
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"

order_status = OrderStatus.SHIPPED

if order_status == OrderStatus.SHIPPED:
    print("Tracking information available.")

print("-" * 50)
class PaymentMethod(Enum):
    CREDIT_CARD = "Credit Card"
    PAYPAL = "PayPal"
    APPLE_PAY = "Apple Pay"


def process_payment(method: PaymentMethod):
    print(f"Processing payment using {method.value}")

# using paypal
process_payment(PaymentMethod.PAYPAL)
# using credit card
process_payment(PaymentMethod.CREDIT_CARD)
# apple pay 
process_payment(PaymentMethod.APPLE_PAY)


print("-" * 50)
class Agent(Enum):
    RESEARCH = "research"
    CODING = "coding"
    WRITER = "writer"
    DEEP_AGENT = "deep agent"

next_agent = Agent.CODING

if next_agent == Agent.RESEARCH:
    print("Routing to the research agent")
elif next_agent == Agent.CODING:
    print("Routing to coding agent")
elif next_agent == Agent.WRITER:
    print("Routing to writer agent")
else:
    print("Unknown agent")


print("-" * 50)

light = TrafficLight.RED

if light == TrafficLight.RED:
    print("Pedestrian must stop")
elif light == TrafficLight.YELLOW:
    print("Pedestrian must slow down")
elif light == TrafficLight.GREEN:
    print("Pedestrian can cross!")
else:
    print("Please wait!")


print("-" * 50)

class FlightMode(Enum):
    TAKEOFF = "Takeoff"
    HOVER = "Hover"
    LAND = "Land"
    RETURN_HOME = "Return Home"

mode = FlightMode.RETURN_HOME

if mode == FlightMode.RETURN_HOME:
    print("Drone returning to launch point.")

print("-" * 50)

class SeatClass(Enum):
    ECONOMY = "Economy"
    BUSINESS = "Business"
    FIRST_CLASS = "First Class"

seat = SeatClass.BUSINESS

if seat == SeatClass.BUSINESS:
    print("Access to business lounge granted.")


print("-" * 50)
class DeviceState(Enum):
    ON = "On"
    OFF = "Off"

living_room_light = DeviceState.ON

if living_room_light == DeviceState.ON:
    print("The living room light is turned on.")