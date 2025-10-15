class Member:
    # PRIVATE MemberName: STRING
    # PRIVATE MemberID : INTEGER
    # PRIVATE SubscriptionPaid : BOOLEAN
    def __init__(self):
        self.__MemberName = ""
        self.__MemberID = ""
        self.__SubscriptionPaid = False

    def SetMemberName(self, MemberP):
        self.__MemberName = MemberP

    def SetMemberID(self, MemberIDP):
        self.__MemberID = MemberIDP

    def SetSubscriptionPaid(self, SubscriptionPaidP):
        self.__SubscriptionPaid = SubscriptionPaidP


class JuniorMember(Member):
    # PRIVATE DateOfBirth : STRING
    def __init__(self):
        super().__init__()
        self.__DateOfBirth = ""

    def SetDateOfBirth(self, Date):
        self.__DateOfBirth = Date

    def SetMemberName(self, MemberP):
        super().SetMemberName(MemberP)

    def SetMemberID(self, MemberIDP):
        super().SetMemberID(MemberIDP)

    def SetSubscriptionPaid(self, SubscriptionPaidP):
        super().SetSubscriptionPaid(SubscriptionPaidP)


intern = JuniorMember()
intern.SetDateOfBirth(2005)
intern.SetMemberName("Muhammad")
intern.SetMemberID(24)
intern.SetSubscriptionPaid(True)