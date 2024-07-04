import 'package:flutter/material.dart';
import 'package:client_testing2/fetchapigames.dart';

class Homepage extends StatefulWidget {
  final String token;

  const Homepage({Key? key, required this.token}) : super(key: key);

  @override
  _HomepageState createState() => _HomepageState();
}

class _HomepageState extends State<Homepage> {
  late Future<List<Game>> futureGames;

  @override
  void initState() {
    super.initState();
    futureGames = fetchGames();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Games List'),
      ),
      body: FutureBuilder<List<Game>>(
        future: futureGames,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return Center(child: Text('No games found'));
          } else {
            return ListView.builder(
              itemCount: snapshot.data!.length,
              itemBuilder: (context, index) {
                final game = snapshot.data![index];
                return ListTile(
                  title: Text(game.name),
                  subtitle: Text(game.genre),
                  trailing: game.imageUrl.isNotEmpty
                      ? Image.network(game.imageUrl, width: 50, height: 50)
                      : Icon(Icons.image_not_supported),
                  onTap: () {
                    // Handle tap, e.g., navigate to a detail screen
                  },
                );
              },
            );
          }
        },
      ),
    );
  }
}
