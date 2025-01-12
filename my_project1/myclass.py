class DataCenter:
    def __init__(self, name, code, location):
        self.dcname = name
        self.dccode = code
        self.location = location
        self.rooms = []  # Room 객체를 저장할 리스트

    def add_room(self, room):
        self.rooms.append(room)

    def total_power_consumption(self):
        return sum(room.total_power_consumption() for room in self.rooms)

    def total_device_count(self):
        return sum(room.total_device_count() for room in self.rooms)

    def status_report(self):
        report = f"Data Center: {self.dccode} ({self.dcname} - {self.location})\n"
        report += f"Total Rooms: {len(self.rooms)}\n"
        report += f"Total Devices: {self.total_device_count()}\n"
        report += f"Total Power Consumption: {self.total_power_consumption()}W\n"
        for room in self.rooms:
            report += f"  {room}\n"
        return report

    def __str__(self):
        return f"DataCenter(name={self.dcname}, code={self.dccode}, location={self.location}, rooms={len(self.rooms)})"


class Room:
    def __init__(self, name):
        self.room_name = name
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def total_power_consumption(self):
        return sum(row.total_power_consumption() for row in self.rows)

    def total_device_count(self):
        return sum(row.total_device_count() for row in self.rows)

    def __str__(self):
        return f"Room(room_name={self.room_name}, rows={len(self.rows)})"


class Row:
    def __init__(self, name):
        self.row_name = name
        self.racks = []

    def add_rack(self, rack):
        self.racks.append(rack)

    def total_power_consumption(self):
        return sum(rack.power_consumption() for rack in self.racks)

    def total_device_count(self):
        return sum(len(rack.devices) for rack in self.racks)

    def __str__(self):
        return f"Row(row_id={self.row_name}, racks={len(self.racks)})"


class Rack:
    def __init__(self, rack_cid, max_devices=20):
        self.rack_cid = rack_cid
        self.devices = []
        self.max_devices = max_devices
        self.power_capacity = 2000  # Watts

    def add_device(self, device):
        if len(self.devices) >= self.max_devices:
            raise ValueError(f"Rack {self.rack_id}에 더 이상 장치를 추가할 수 없습니다!")
        self.devices.append(device)

    def remove_device(self, device_id):
        self.devices = [d for d in self.devices if d.device_id != device_id]

    def is_overloaded(self):
        return self.power_consumption() > self.power_capacity

    def power_consumption(self):
        return sum(device.power_usage for device in self.devices)

    def __str__(self):
        return f"Rack(rack_id={self.rack_cid}, devices={len(self.devices)}, max_devices={self.max_devices})"


class Device:
    def __init__(self, device_id, device_type, power_usage, status="active"):
        self.device_id = device_id
        self.device_type = device_type  # 예: "Server", "Switch"
        self.power_usage = power_usage  # Watts
        self.status = status  # "active", "inactive", "maintenance"

    def deactivate(self):
        self.status = "inactive"

    def activate(self):
        self.status = "active"

    def is_active(self):
        return self.status == "active"

    def __str__(self):
        return f"Device(device_id={self.device_id}, type={self.device_type}, power={self.power_usage}W, status={self.status})"
