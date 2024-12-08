class Uper:
    def __init__(self):
        self.ListerName: list = []
        self.ListerValue: list = []
        self.ListerHour: list = []
        self.ListerDate: list = []
        self.ListerAll: list = []
    def New_Value(self, Name, Value, Time, Date):
        self.ListerName.append(Name)
        self.ListerValue.append(Value)
        self.ListerHour.append(Time)
        self.ListerDate.append(Date)
        self.ListerAll.append(f'{Name}:{Value} -> {Date}-{Time}')
    def PushValue(self):
        return self.ListerValue
    def PushName(self):
        return self.ListerName
    def PushTime(self):
        return self.ListerHour
    def PushDate(self):
        return self.ListerDate
    def PushAll(self):
        return self.ListerAll
class Lower:
    def __init__(self):
        self.ListerName: list = []
        self.ListerValue: list = []
        self.ListerHour: list = []
        self.ListerDate: list = []
        self.ListerAll: list = []
    def New_Value(self, Name, Value, Time, Date):
        self.ListerName.append(Name)
        self.ListerValue.append(Value)
        self.ListerHour.append(Time)
        self.ListerDate.append(Date)
        self.ListerAll.append(f'{Name}:{Value} -> {Date}-{Time}')
    def PushValue(self):
        return self.ListerValue
    def PushName(self):
        return self.ListerName
    def PushTime(self):
        return self.ListerHour
    def PushDate(self):
        return self.ListerDate
    def PushAll(self):
        return self.ListerAll
class Peak:
    def __init__(self):
        self.ListerName: list = []
        self.ListerValue: list = []
        self.ListerHour: list = []
        self.ListerDate: list = []
        self.ListerAll: list = []
    def New_Value(self, Name, Value, Time, Date):
        self.ListerName.append(Name)
        self.ListerValue.append(Value)
        self.ListerHour.append(Time)
        self.ListerDate.append(Date)
        self.ListerAll.append(f'{Name}:{Value} -> {Date}-{Time}')
    def PushValue(self):
        return self.ListerValue
    def PushName(self):
        return self.ListerName
    def PushTime(self):
        return self.ListerHour
    def PushDate(self):
        return self.ListerDate
    def PushAll(self):
        return self.ListerAll
class Decline:
    def __init__(self):
        self.ListerName: list = []
        self.ListerValue: list = []
        self.ListerHour: list = []
        self.ListerDate: list = []
        self.ListerAll: list = []
    def New_Value(self, Name, Value, Time, Date):
        self.ListerName.append(Name)
        self.ListerValue.append(Value)
        self.ListerHour.append(Time)
        self.ListerDate.append(Date)
        self.ListerAll.append(f'{Name}:{Value} -> {Date}-{Time}')
    def PushValue(self):
        return self.ListerValue
    def PushName(self):
        return self.ListerName
    def PushTime(self):
        return self.ListerHour
    def PushDate(self):
        return self.ListerDate
    def PushAll(self):
        return self.ListerAll

class Estable:
    def __init__(self):
        self.ListerName: list = []
        self.ListerValue: list = []
        self.ListerHour: list = []
        self.ListerDate: list = []
        self.ListerAll: list = []
    def New_Value(self, Name, Value, Time, Date):
        self.ListerName.append(Name)
        self.ListerValue.append(Value)
        self.ListerHour.append(Time)
        self.ListerDate.append(Date)
        self.ListerAll.append(f'{Name}:{Value} -> {Date}-{Time}')
    def PushValue(self):
        return self.ListerValue
    def PushName(self):
        return self.ListerName
    def PushTime(self):
        return self.ListerHour
    def PushDate(self):
        return self.ListerDate
    def PushAll(self):
        return self.ListerAll

class Unstable:
    def __init__(self):
        self.ListerName: list = []
        self.ListerValue: list = []
        self.ListerHour: list = []
        self.ListerDate: list = []
        self.ListerAll: list = []
    def New_Value(self, Name, Value, Time, Date):
        self.ListerName.append(Name)
        self.ListerValue.append(Value)
        self.ListerHour.append(Time)
        self.ListerDate.append(Date)
        self.ListerAll.append(f'{Name}:{Value} -> {Date}-{Time}')
    def PushValue(self):
        return self.ListerValue
    def PushName(self):
        return self.ListerName
    def PushTime(self):
        return self.ListerHour
    def PushDate(self):
        return self.ListerDate
    def PushAll(self):
        return self.ListerAll