import 'dart:convert';
import 'package:http/http.dart' as http;

class Game {
  final int id;
  final String name;
  final String genre;
  final String imageUrl;
  final String description;
  final DateTime createdAt;

  Game({
    required this.id,
    required this.name,
    required this.genre,
    required this.imageUrl,
    required this.description,
    required this.createdAt,
  });

  factory Game.fromJson(Map<String, dynamic> json) {
    // print("")
    return Game(
      id: json['id_game'],
      name: json['nama_game'],
      genre: json['genre_game'],
      imageUrl: json['images_game'],
      description: json['descriptions_game'],
      createdAt: DateTime.parse(json['created_at']),
    );
  }
}

Future<List<Game>> fetchGames() async {
  final response = await http.get(
    Uri.parse('http://127.0.0.1:8000/api/games/'),
  );

  if (response.statusCode == 200) {
    List jsonResponse = json.decode(response.body);
    return jsonResponse.map((game) => Game.fromJson(game)).toList();
  } else {
    print('Failed to load games: ${response.statusCode}');
    throw Exception('Gagal Load Game');
  }
}
