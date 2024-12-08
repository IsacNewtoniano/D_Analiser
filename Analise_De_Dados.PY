from ValoresDefinidos import Uper, Lower, Peak, Decline, Estable, Unstable
from collections import deque
class Dados:
    def __init__(self, Limit):
        # Objects Values
        self.Object_Name: str = ''
        self.Object_Time: str = ''
        self.Object_Value: int = 0
        self.Object_Date: str = ''
        # Itens Verifiers
        self.Index: int = 0
        self.DItens: int = 0
        self.Average: int = 0
        self.Object: list = []
        self.Itens = deque(maxlen=Limit)
        self.Values = deque(maxlen=Limit)
        # Class For Delimiters
        self.vUper = Uper()
        self.vLower = Lower()
        self.vPeak = Peak()
        self.vDecline = Decline()
        self.vEstable = Estable()
        self.vUnstable = Unstable()
        # Delimiters
        self.dUper = 110
        self.dLower = 20
        self.dPeak = 140
        self.dDecline = 40
        self.dUnstableBigger = 150
        self.dUnstableLess = 50

    def Bigger(self,Name, Time, Date, Value, Average):
        VM = Value / Average * 100
        print(VM)
        if VM > self.dUnstableBigger:
            self.vUnstable.New_Value(Name, Value, Time, Date)
        if VM > self.dPeak:
            self.vPeak.New_Value(Name, Value, Time, Date)
        if VM > self.dUper:
            self.vUper.New_Value(Name, Value, Time, Date)
        else:
            self.vEstable.New_Value(Name, Value, Time, Date)
    def Less(self, Name, Value, Time, Date, Average):
        VM = Value / Average * 100
        print(VM, 'AI', self.dLower)
        if VM > self.dUnstableLess:
            self.vUnstable.New_Value(Name, Value, Time, Date)
        if VM > self.dDecline:
            self.vDecline.New_Value(Name, Value, Time, Date)
        if VM > self.dLower:
            self.vLower.New_Value(Name, Value, Time, Date)
        else:
            self.vEstable.New_Value(Name, Value, Time, Date)
    def Verifiery(self):
        Name: str = self.Object[self.Object_Name]
        Value: float|int = self.Object[self.Object_Value]
        Time: str = self.Object[self.Object_Time]
        Date: str = self.Object[self.Object_Date]
        Average = self.Average
        if Value >= Average:
            self.Bigger(Name, Time, Date, Value, Average)
        elif Value < Average:
            self.Less(Name, Value, Time, Date, Average)
    def Init(self, Entrada: list):
        for iten in Entrada:
            self.Object = iten
            self.Itens.append(iten)
            self.Values.append(self.Object[1])
            self.DItens = len(self.Values)
            self.Average = sum(self.Values) / self.DItens
            self.Verifiery()
    def Push(self, VarPush, TypePush):
        match VarPush:
            case 'Uper':
                match TypePush:
                    case 'Value':
                        return self.vUper.PushValue()
                    case 'Name':
                        return self.vUper.PushName()
                    case 'Time':
                        return self.vUper.PushTime()
                    case 'Date':
                        return self.vUper.PushDate()
                    case 'All':
                        return self.vUper.PushAll()
            case 'Lower':
                match TypePush:
                    case 'Value':
                        return self.vLower.PushValue()
                    case 'Name':
                        return self.vLower.PushName()
                    case 'Time':
                        return self.vLower.PushTime()
                    case 'Date':
                        return self.vLower.PushDate()
                    case 'All':
                        return self.vLower.PushAll()
            case 'Peak':
                match TypePush:
                    case 'Value':
                        return self.vPeak.PushValue()
                    case 'Name':
                        return self.vPeak.PushName()
                    case 'Time':
                        return self.vPeak.PushTime()
                    case 'Date':
                        return self.vPeak.PushDate()
                    case 'All':
                        return self.vPeak.PushAll()
            case 'Decline':
                match TypePush:
                    case 'Value':
                        return self.vDecline.PushValue()
                    case 'Name':
                        return self.vDecline.PushName()
                    case 'Time':
                        return self.vDecline.PushTime()
                    case 'Date':
                        return self.vDecline.PushDate()
                    case 'All':
                        return self.vDecline.PushAll()
            case 'Estable':
                match TypePush:
                    case 'Value':
                        return self.vEstable.PushValue()
                    case 'Name':
                        return self.vEstable.PushName()
                    case 'Time':
                        return self.vEstable.PushTime()
                    case 'Date':
                        return self.vEstable.PushDate()
                    case 'All':
                        return self.vEstable.PushAll()
            case 'Unstable':
                match TypePush:
                    case 'Value':
                        return self.vUnstable.PushValue()
                    case 'Name':
                        return self.vUnstable.PushName()
                    case 'Time':
                        return self.vUnstable.PushTime()
                    case 'Date':
                        return self.vUnstable.PushDate()
                    case 'All':
                        return self.vUnstable.PushAll()
    def ValueConfig(self, _Uper, _Lower, _Peak, _Decline, _UnstableBigger, _UnstableLess):
        self.dUper = _Uper
        self.dLower = _Lower
        self.dPeak = _Peak
        self.dDecline = _Decline
        self.dUnstableBigger = _UnstableBigger
        self.dUnstableLess = _UnstableLess
    def PositionConfig(self, Object_Name, Object_Value, Object_Time, Object_Date):
        self.Object_Name = Object_Name
        self.Object_Value = Object_Value
        self.Object_Time = Object_Time
        self.Object_Date = Object_Date