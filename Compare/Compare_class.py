class Compare:

    def print_eternity(key, json1, json2):
        if (type(json1[key]) is str) and (key != "rc_updated_at") and (key != "changed_time_at") and (key != "program_updated_at") and (key != "time"):
            print()
            print("mismatch")
            print("in plan", key, " is ", json1[key])
            print("in fact", key, " is ", json2.get(key))
            return "incident"
        if type(json1[key]) is list:
            print()
            print("mismatch")
            print("in plan", key, " are: ")
            for i in json1["phases"]:
                if type(i) is list:
                    for k in i:
                        print(k)
                else:
                    print(i)
            print("in fact", key, " are: ")
            for i in json2.get("phases"):
                if type(i) is list:
                    for k in i:
                        print(k)
                else:
                    print(i)
            return "incident"
    @classmethod
    def compare_dicts(self, json1, json2):
        for key in json1:
            if (json1[key] != json2.get(key)):
                self.print_eternity(key,json1,json2)

