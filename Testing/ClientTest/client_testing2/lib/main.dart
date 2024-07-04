import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:client_testing2/homepege.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget adalah root dari aplikasi Anda.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Login Demo',
      home: LoginPage(),
    );
  }
}

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  TextEditingController emailController = TextEditingController();
  TextEditingController passwordController = TextEditingController();

  void login() async {
    String email = emailController.text;
    String password = passwordController.text;

    var url =
        'http://127.0.0.1:8000/api/auth/login/'; // Sesuaikan dengan URL API login Anda
    var response = await http.post(
      Uri.parse(url),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({
        'email': email,
        'password': password,
      }),
    );

    if (response.statusCode == 200) {
      var responseData = json.decode(response.body);

      // Pastikan bahwa responseData adalah Map dan memiliki kunci 'token'
      if (responseData is Map<String, dynamic> &&
          responseData.containsKey('token')) {
        var tokenData = responseData['token'];

        // Pastikan bahwa tokenData adalah Map dan memiliki kunci 'access'
        if (tokenData is Map<String, dynamic> &&
            tokenData.containsKey('access')) {
          String token = tokenData['access'];
          // Simpan token atau lakukan sesuatu dengan token ini
          // print('Login berhasil. Token: $token');

          // Navigasi ke halaman berikutnya setelah login berhasil
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => Homepage(token: token)),
          );
        } else {
          print('Error: access token not found in response');
        }
      } else {
        print('Error: token not found in response');
      }
    } else {
      print('Gagal login. Status code: ${response.statusCode}');
      // Tampilkan pesan kesalahan atau lakukan sesuatu yang sesuai
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Login'),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            TextField(
              controller: emailController,
              decoration: InputDecoration(
                labelText: 'Email',
              ),
            ),
            SizedBox(height: 12.0),
            TextField(
              controller: passwordController,
              decoration: InputDecoration(
                labelText: 'Password',
              ),
              obscureText: true,
            ),
            SizedBox(height: 24.0),
            ElevatedButton(
              onPressed: login,
              child: Text('Login'),
            ),
          ],
        ),
      ),
    );
  }
}
