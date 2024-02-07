import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class AddCarScreen extends StatefulWidget {
  final VoidCallback? onActivityAdded;

  const AddCarScreen({Key? key, this.onActivityAdded}) : super(key: key);

  @override
  _AddCarScreenState createState() => _AddCarScreenState();
}

class _AddCarScreenState extends State<AddCarScreen> {
  final _formKey = GlobalKey<FormState>();

  TextEditingController _nameController = TextEditingController();
  TextEditingController _dateController = TextEditingController();
  TextEditingController _detailsController = TextEditingController();
  TextEditingController _statusController = TextEditingController();
  TextEditingController _participantsController = TextEditingController();
  TextEditingController _typeController = TextEditingController();

  @override
  void dispose() {
    _nameController.dispose();
    _dateController.dispose();
    _detailsController.dispose();
    _statusController.dispose();
    _participantsController.dispose();
    _typeController.dispose();
    super.dispose();
  }

  Future<void> _addActivity() async {
    if (_formKey.currentState!.validate()) {
      final name = _nameController.text.trim();
      final date = _dateController.text.trim();
      final details = _detailsController.text.trim();
      final status = _statusController.text.trim();
      final type = _typeController.text.trim();
      final participants = int.parse(_participantsController.text.trim());

      final url = Uri.parse("http://10.0.2.2:2407/activity");

      try {
        final response = await http.post(
          url,
          body: {
            'name': name,
            'date': date,
            'details': details,
            'status': status,
            'participants': participants.toString(),
            'type': type,
          },
        );

        if (response.statusCode == 200) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text('Activity added successfully: $name, $date, $details, $status, $participants, $type'),
            ),
          );

          // Call the callback function to notify the parent widget
          widget.onActivityAdded?.call();

          // Navigate back to the previous screen
          Navigator.of(context).pop();
        } else {
          // Error adding book
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text('Failed to add activity'),
            ),
          );
        }
      } catch (e) {
        // Error communicating with server
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Error: $e'),
          ),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Add New Activity'),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: EdgeInsets.all(16.0),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                TextFormField(
                  controller: _nameController,
                  decoration: InputDecoration(labelText: 'Name'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter a name';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _dateController,
                  decoration: InputDecoration(labelText: 'Date'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter a supplier';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _detailsController,
                  decoration: InputDecoration(labelText: 'Details'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter details';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _statusController,
                  decoration: InputDecoration(labelText: 'Status'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter a status';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _participantsController,
                  keyboardType: TextInputType.number,
                  decoration: InputDecoration(labelText: 'Participants'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter number of participants';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _typeController,
                  decoration: InputDecoration(labelText: 'Type'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter a type';
                    }
                    return null;
                  },
                ),
                SizedBox(height: 20),
                ElevatedButton(
                  onPressed: _addActivity,
                  child: Text('Add Activity'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
