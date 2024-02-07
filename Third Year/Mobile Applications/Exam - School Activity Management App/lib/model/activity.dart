class Activity {
  int id;
  String name;
  String date;
  String details;
  String status;
  int participants;
  String type;

  Activity({
    required this.id,
    required this.name,
    required this.date,
    required this.details,
    required this.status,
    required this.participants,
    required this.type,
  });

  factory Activity.fromJson(Map<String, dynamic> json) {
    return Activity(
      id: json['id'],
      name: json['name'],
      date: json['date'],
      details: json['details'],
      status: json['status'],
      participants: int.parse(json['participants'].toString()),
      type: json['type'],
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'name': name,
      'date': date,
      'details': details,
      'status': status,
      'participants': participants,
      'type': type,
    };
  }
}

class ActivityDTO {
  String name;
  String date;
  String details;
  String status;
  int participants;
  String type;

  ActivityDTO({
    required this.name,
    required this.date,
    required this.details,
    required this.status,
    required this.participants,
    required this.type,
  });

  factory ActivityDTO.fromJson(Map<String, dynamic> json) {
    return ActivityDTO(
      name: json['name'],
      date: json['date'],
      details: json['details'],
      status: json['status'],
      participants: json['participants'],
      type: json['type'],
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'name': name,
      'date': date,
      'details': details,
      'status': status,
      'participants': participants,
      'type': type,
    };
  }
}