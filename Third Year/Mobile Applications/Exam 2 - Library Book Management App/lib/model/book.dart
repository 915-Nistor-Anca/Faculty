class Book {
  int id;
  String title;
  String author;
  String genre;
  String availability;
  int year;
  String ISBN;

  Book({
    required this.id,
    required this.title,
    required this.author,
    required this.genre,
    required this.availability,
    required this.year,
    required this.ISBN,
  });

  factory Book.fromJson(Map<String, dynamic> json) {
    return Book(
      id: json['id'],
      title: json['title'],
      author: json['author'],
      genre: json['genre'],
      availability: json['availability'],
      year: int.parse(json['year'].toString()),
      ISBN: json['ISBN'],
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'title': title,
      'author': author,
      'genre': genre,
      'availability': availability,
      'year': year,
      'ISBN': ISBN,
    };
  }
}

class BookDTO {
  String title;
  String author;
  String genre;
  String availability;
  int year;
  String ISBN;

  BookDTO({
    required this.title,
    required this.author,
    required this.genre,
    required this.availability,
    required this.year,
    required this.ISBN,
  });

  factory BookDTO.fromJson(Map<String, dynamic> json) {
    return BookDTO(
      title: json['title'],
      author: json['author'],
      genre: json['genre'],
      availability: json['availability'],
      year: json['year'],
      ISBN: json['ISBN'],
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'title': title,
      'author': author,
      'genre': genre,
      'availability': availability,
      'year': year,
      'ISBN': ISBN,
    };
  }
}