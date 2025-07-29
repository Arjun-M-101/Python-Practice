class AppV1:
    def version1(self):
        return "This is version 1 of the app."
class AppV2(AppV1):
    def version2(self):
        return "This is version 2 of the app."
deployment = AppV2()
print(deployment.version1())  # Accessing method from AppV1
print(deployment.version2())  # Accessing method from AppV2