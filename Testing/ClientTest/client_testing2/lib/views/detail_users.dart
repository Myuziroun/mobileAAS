import 'package:client_testing2/api/api_detail_user.dart';
import 'package:flutter/material.dart';
import 'dart:convert';

class userDetailsPage extends StatefulWidget {
  final String accessToken;
  userDetailsPage({required this.accessToken});
  @override
  _userDetailsPageState createState() => _userDetailsPageState();
}

class _userDetailsPageState extends State<userDetailsPage> {
  late Future<List<userDetails>> futureUserDetails;

  @override
  void initState() {
    super.initState();
    futureUserDetails = fetchUserDetails(widget.accessToken);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('User Details'),
      ),
      body: FutureBuilder<List<userDetails>?>(
        future: futureUserDetails,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return Center(child: Text('No details Found'));
          } else {
            return ListView.builder(
              itemCount: snapshot.data!.length,
              itemBuilder: (context, index) {
                final detail = snapshot.data![index];
                return ListTile(
                  title: Text('Game ID: ${detail.id_game}'),
                  subtitle: Text('Created at: ${detail.created_at}'),
                );
              },
            );
          }
        },
      ),
    );
  }
}
