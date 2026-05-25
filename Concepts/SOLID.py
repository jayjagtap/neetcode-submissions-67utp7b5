# 🎯 GOAL: Internalize all 5 SOLID principles with bad vs good code examples

# 📝 PRINCIPLES:
# • S — Single Responsibility: one reason to change
# • O — Open/Closed: open for extension, closed for modification
# • L — Liskov Substitution: subclass must be substitutable
# • I — Interface Segregation: no fat interfaces
# • D — Dependency Inversion: depend on abstractions


# You're given this class. Identify how many responsibilities it has, name them, and write the refactored version splitting them apart.


class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self):
        # computes statistics from self.data
        total = sum(self.data)
        avg = total / len(self.data)
        return {"total": total, "avg": avg}

    def format_as_html(self, report):
        return f"<h1>Total: {report['total']}</h1><p>Avg: {report['avg']}</p>"

    def save_to_file(self, html, filename):
        with open(filename, "w") as f:
            f.write(html)

"""
Answer: The ReportGenerator class has 3 responsibilites. 
First one to generate report, second one to format and the 3rd is to save the file.
With the single responsibility principle, it should be in a different class, so only 1 responsibility
"""

class ReportGenerator:

    def __init__(self, data):
        self.data = data 

    def generate_report(self):
        # computes statistics from self.data
        total = sum(self.data)
        avg = total / len(self.data)
        return {"total": total, "avg": avg}

class ReportFormatter:

    def format_report_html(self, report):
        return f"<h1>Total: {report['total']}</h1><p>Avg: {report['avg']}</p>"
    

class ReportFileWriter:

    def save(self, html, file_name):
        with open(file_name, "w") as f:
            f.write(html)
    


"""
Open Closed Principle. Open for extension. Closed for modification
Gotcha: The abstraction has to be designed upfront (or refactored in). OCP doesn't mean "never edit code" — it means stable, tested code shouldn't need to change just because requirements grow. The abc.ABC + @abstractmethod pattern is Python's idiomatic way to enforce the contract.
"""

"""
Puzzle: This notification system violates OCP. Refactor it so adding a new channel (say, Slack) requires zero changes to existing code.
class Notifier:
    def send(self, channel, message):
        if channel == "email":
            print(f"Sending email: {message}")
        elif channel == "sms":
            print(f"Sending SMS: {message}")
        # to add Slack: edit this method ← bad

SOLID — Plain Language Recap
S — Single Responsibility
Every class should have one job, owned by one "stakeholder." The test: ask "who would ask me to change this?" If the answer is two different people — a DBA and a marketing manager, for example — split the class. Blast radius stays small when things change.
O — Open/Closed
You should be able to add new behaviour without editing code that already works. The pattern is always the same: abstract base class defines the contract, new behaviour = new subclass. If you're adding elif branches to an existing method every time a requirement changes, that's the smell.
L — Liskov Substitution
A subclass must keep every promise its parent made. If you can't drop a subclass in wherever the parent is used without something breaking, the inheritance is lying. The giveaway is raise NotImplementedError in a subclass — that's a parent promise the child can't honour. Fix: restructure the hierarchy so the base class only promises what's universally true.
I — Interface Segregation
Don't force a class to implement methods it doesn't need. Keep interfaces small and focused. A Robot shouldn't have to implement eat_lunch() just because it shares an interface with humans. Split the interface, compose via multiple inheritance. Same giveaway as LSP: raise NotImplementedError — but here the fix is splitting the interface, not the hierarchy.
D — Dependency Inversion
High-level business logic shouldn't care which specific tool it's using. Inject dependencies through __init__ and type-hint against the abstraction, not the concrete class. The payoff is twofold: you can swap implementations without touching business logic, and you can pass mocks in tests without spinning up real databases or email servers.

The thread connecting all five:

Depend on abstractions. Keep things small and focused. Never touch working code to add new behaviour.

When you walk into a system design interview and they ask "how would you make this extensible / testable / maintainable" — SOLID is the vocabulary for your answer.

"""


from abc import ABC, abstractmethod

from .SOLID import ReportGenerator


class Notifier(ABC):

    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(Notifier):

    def send(self, message):
        print(f"Sending email: {message}")

class SMSNotifier(Notifier):

    def send(self, message):
        print(f"Sending SMS: {message}")

class SlackNotifier(Notifier):

    def send(self, message):
        print(f"Sending Slack Message: {message}")


message = "Hello, this is a notification"

slackNotification = SlackNotifier()

print(slackNotification.send(message))


"""
Liskov Substitution method, subclassed should always keep the promises their parents made
Classic Violation: Subclass inherits a method but does not honor it and throws a exception
"""

"""
Puzzle: This code has a classic LSP violation. Identify why substitution breaks, then fix the hierarchy:
"""

class Shape:
    def area(self) -> float: ...
    def resize(self, factor: float) -> None: ...

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def resize(self, factor):
        self.w *= factor
        self.h *= factor

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def resize(self, factor):
        self.side *= factor


def scale_and_print(shape: Rectangle, factor: float):
    original = shape.area()
    # print(original)
    shape.w = 10   # caller assumes independent sides
    shape.h = 5
    print(shape.area())  # expects 50

scale_and_print(Square(4), 2)  # what prints, and why is it wrong?

"""
I - Interface Segregation Principle. 

If the interface is fat and subclassed cannot implement all methods, split it.

Dont force a class to implement methods it does not need.
Gotcha: ISP and LSP violations often show up together. 
When you see raise NotImplementedError in a subclass, ask yourself two questions: is the hierarchy wrong (LSP), or is the interface too fat (ISP)? Usually it's ISP — the fix is to split the interface, not restructure inheritance.
"""

class Worker(ABC):
    @abstractmethod
    def work(self): ...

class WorkerActivities(ABC):
    @abstractmethod
    def eat_lunch(self): ...

    @abstractmethod
    def take_break(self): ...

class RobotWorker(Worker):
    def work(self):
        print("Robot working...")

class HumanWorker(Worker, WorkerActivities):
    """
    Implement all 3 methods
    """
    pass


"""
Dependency Inversion Pricinple

High Level modules should not depend on low level modules. Both should depend on abstrations.

Dependency Injection is technique to achieve Dependency Inversion
"""



"""
This ReportService is hardwired to PDFExporter. 
Refactor it so you can export to PDF, CSV, or any future format — without ever touching ReportService again:

class PDFExporter:
    def export(self, data):
        print(f"Exporting to PDF: {data}")

class ReportService:
    def __init__(self):
        self.exporter = PDFExporter()  # hardwired ← bad

    def generate(self, data):
        self.exporter.export(data)
"""

from abc import ABC, abstractmethod
class Exporter(ABC):
    @abstractmethod
    def export(self, data):
        pass


class PDFExporter(Exporter):

    def export(self, data):
        print(f"Exporting to PDF: {data}")


class CSVExporter(Exporter):

    def export(self, data):
        print(f"Exporting to CSV: {data}")

class ReportService:
    def __init__(self, exporter: Exporter):  # Dependency Injection
        self.exporter = exporter 

    def generate(self, data):
        self.exporter.export(data)


# swap exporters — ReportService never changes
ReportService(PDFExporter()).generate("Q3 Sales")
ReportService(CSVExporter()).generate("Q3 Sales")


"""
Combo Puzzle

You're building a notification and reporting system for an e-commerce platform. Here's the brief:

Orders come in and need to be saved somewhere
A report gets generated from order data
The report gets exported in different formats
A notification gets sent when an order is placed
New export formats and notification channels will be added in future


class OrderSystem:
    def __init__(self):
        self.orders = []

    def process_order(self, order):
        # save
        self.orders.append(order)

        # generate + format report
        total = sum(order["items"])
        report = f"<h1>Total: {total}</h1>"

        # export report
        with open("report.pdf", "w") as f:
            f.write(report)

        # notify
        print(f"Sending email: Order {order['id']} confirmed")
        print(f"Sending SMS: Order {order['id']} confirmed")
"""

from abc import ABC, abstractmethod

class Orders:
    def __init__(self, 
                 exporter: Exporter, 
                 reportGenerator: ReportGenerator, notifier: list(NotificationSystem)):
        self.orders = []
        self.exporter = exporter
        self.reportGenerator = reportGenerator
        self.notifiers = notifiers

    def process_order(self, order):
        # sav
        self.orders.append(order)

        # Generate Report
        self.reportGenerator.generateReport(order)

        # export report
        self.exporter.export(order)

        # # notify
        self.notificationSystem.sendNotification(order)


class ReportGenerator(ABC):
    
    @abstractmethod
    def generateReport(self, orders: Orders):
        pass

    @abstractmethod
    def formatReport(self, total):
        pass

class NotificationSystem(ABC):
    
    @abstractmethod
    def sendNotification(self, order):
        pass

class Exporter(ABC):

    @abstractmethod
    def exportReport(self, report: ReportGenerator):
        pass

class HtmlReportGenerator(ReportGenerator):

    total = None

    def generatetReport(self, order: Orders):
         # generate + format report
        self.total = sum(order["items"])
       
        
    def FormatReport(self, total: float):
        report = f"<h1>Total: {total}</h1>"
        return report
    
class EmailNotificationSystem(NotificationSystem):

    def sendNotification(self, order):
        print(f"Sending email: Order {order['id']} confirmed")
        
class SMSNotificationSystem(NotificationSystem):

    def sendNotification(self, order):
        print(f"Sending SMS: Order {order['id']} confirmed")

class PdfExporter(Exporter):

    def exportReport(report: ReportGenerator):
        with open("report.pdf", "w") as f:
            f.write(report)

"""
SOLID principles used: Single Responsibility: break ReportGenerator, NotificationSystem, Exporter from process() 
into separate abstract classes. Orders should only be responsible for orders

HtmlReportGenerator and NotificationSystem are open for extension but closed for modification.

"""