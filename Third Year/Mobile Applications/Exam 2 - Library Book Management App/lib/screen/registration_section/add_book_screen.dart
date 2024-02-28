import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class AddActivityScreen extends StatefulWidget {
  final VoidCallback? onActivityAdded;

  const AddActivityScreen({Key? key, this.onActivityAdded}) : super(key: key);

  @override
  _AddActivityScreenState createState() => _AddActivityScreenState();
}

class _AddActivityScreenState extends State<AddActivityScreen> {
  final _formKey = GlobalKey<FormState>();

  TextEditingController _titleController = TextEditingController();
  TextEditingController _authirController = TextEditingController();
  TextEditingController _genreController = TextEditingController();
  TextEditingController _availabilityController = TextEditingController();
  TextEditingController _yearController = TextEditingController();
  TextEditingController _isbnController = TextEditingController();

  @override
  void dispose() {
    _titleController.dispose();
    _authirController.dispose();
    _genreController.dispose();
    _availabilityController.dispose();
    _yearController.dispose();
    _isbnController.dispose();
    super.dispose();
  }

  Future<void> _addActivity() async {
    if (_formKey.currentState!.validate()) {
      final title = _titleController.text.trim();
      final author = _authirController.text.trim();
      final genre = _genreController.text.trim();
      final availability = _availabilityController.text.trim();
      final isbn = _isbnController.text.trim();
      final year = int.parse(_yearController.text.trim());

      final url = Uri.parse("http://10.0.2.2:2419/book");

      try {
        final response = await http.post(
          url,
          body: {
            'title': title,
            'author': author,
            'genre': genre,
            'availability': availability,
            'year': year.toString(),
            'ISBN': isbn,
          },
        );

        if (response.statusCode == 200) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text('Book added successfully: $title, $author, $genre, $availability, $year, $isbn'),
            ),
          );

          widget.onActivityAdded?.call();

          Navigator.of(context).pop();
        } else {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text('${response.body}'),
            ),
          );
        }
      } catch (e) {
        // Error communicating with server
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('$e'),
          ),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Add New Book'),
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
                  controller: _titleController,
                  decoration: InputDecoration(labelText: 'Title'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter a title';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _authirController,
                  decoration: InputDecoration(labelText: 'Author'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter an author';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _genreController,
                  decoration: InputDecoration(labelText: 'Genre'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter genre';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _availabilityController,
                  decoration: InputDecoration(labelText: 'Availability'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter availability';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _yearController,
                  keyboardType: TextInputType.number,
                  decoration: InputDecoration(labelText: 'Year'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter the year';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _isbnController,
                  decoration: InputDecoration(labelText: 'ISBN'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter ISBN';
                    }
                    return null;
                  },
                ),
                SizedBox(height: 20),
                ElevatedButton(
                  onPressed: _addActivity,
                  child: Text('Add Books'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
