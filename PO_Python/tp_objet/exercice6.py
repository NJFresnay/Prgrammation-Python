#!/bin/env python3

import Instant

instant1 = Instant.Instant(h=1,m=10,s=30)
instant2 = Instant.Instant(m=10,s=30)
instant3 = Instant.Instant(m=10)
print(instant1.__str__())
print(instant2.__str__())
print(instant3.__str__())

if __name__ == "__main__":
    pass
