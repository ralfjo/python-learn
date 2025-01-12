from myclass import DataCenter, Room, Row, Rack, Device

# 데이터 센터 생성
dc1 = DataCenter(name="Seoul DC", code="KR1", location="Seoul")
dc2 = DataCenter(name="Busan DC", code="KR2", location="Busan")

# Room 생성
room1 = Room(name="5FE")
room2 = Room(name="8FA")

# Row 생성
row1 = Row(name="03")
row2 = Row(name="04")

# Rack 생성
rack1 = Rack(rack_cid="03")
rack2 = Rack(rack_cid="04")

# 장치 생성
device1 = Device(device_id="Server-001", device_type="Server", power_usage=300)
device2 = Device(device_id="Switch-001", device_type="Switch", power_usage=100)

# 구조 구성
rack1.add_device(device1)
rack2.add_device(device2)

row1.add_rack(rack1)
row2.add_rack(rack2)

room1.add_row(row1)
room2.add_row(row2)

dc1.add_room(room1)
dc2.add_room(room2)

# 출력
print(dc1.status_report())
print(dc2.status_report())

# 각 요소 정보 확인
print(room1)
print(row1)
print(rack1)
print(device1)



