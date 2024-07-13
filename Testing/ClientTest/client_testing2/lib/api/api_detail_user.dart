import 'dart:convert';
// import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class userDetails {
  final int id_detail_user;
  final int id_user;
  final int id_game;
  final String created_at;

  userDetails(
      {required this.id_detail_user,
      required this.id_user,
      required this.id_game,
      required this.created_at});

  factory userDetails.fromJson(Map<String, dynamic> json) {
    return userDetails(
        id_detail_user: json['id_detail_user'],
        id_user: json['id_user'],
        id_game: json['id_game'],
        created_at: json['created_at']);
  }
}

Future<List<userDetails>> fetchUserDetails(String accessToken) async {
  final response = await http.get(
    Uri.parse('http://127.0.0.1:8000/user-details/'),
    headers: {
      'Authorization': 'Bearer $accessToken',
    },
  );
  if (response.statusCode == 200) {
    List<dynamic> data = json.decode(response.body);
    return data.map((item) => userDetails.fromJson(item)).toList();
  } else {
    throw Exception('failed to load user detials');
  }
}
