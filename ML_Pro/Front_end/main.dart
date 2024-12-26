import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Farmer Helper',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: MyHomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  File? _image;
  final picker = ImagePicker();
  bool _isLoading = false;
  String _responseText = "Server Response will be shown here";
  List<Map<String, dynamic>> _preventionList = [];

  // Function to pick an image
  Future<void> _pickImage() async {
    final pickedFile = await picker.pickImage(source: ImageSource.gallery);

    setState(() {
      if (pickedFile != null) {
        _image = File(pickedFile.path);
      } else {
        print('No image selected.');
      }
    });
  }

  // Function to send the image to the server
  Future<void> _sendImageToServer(File imageFile) async {
    setState(() {
      _isLoading = true;
      _responseText = "Processing...";
      _preventionList = [];
    });

    try {
      var uri = Uri.parse("https://a559-2409-40c2-1223-bfda-c84a-805f-634b-b7e5.ngrok-free.app/uploadfile/"); // Replace with server URL
      var request = http.MultipartRequest('POST', uri);
      request.files.add(
        await http.MultipartFile.fromPath('file', imageFile.path),
      );

      var response = await request.send();

      if (response.statusCode == 200) {
        var responseBody = await response.stream.bytesToString();
        var jsonData = json.decode(responseBody);

        setState(() {
          _isLoading = false;
          _responseText = "Class: ${jsonData['Class']}\n"
              "Probability: ${(jsonData['Probability'] * 100).toStringAsFixed(2)}%";
          _preventionList = _extractHeadingsAndSubpoints(jsonData['Cure_and_Prevention']);
        });
      } else {
        setState(() {
          _isLoading = false;
          _responseText = "Error: Server responded with ${response.statusCode}";
        });
      }
    } catch (e) {
      setState(() {
        _isLoading = false;
        _responseText = "Error: $e";
      });
    }
  }

  // Function to extract headings and subpoints using regular expressions
  List<Map<String, dynamic>> _extractHeadingsAndSubpoints(String text) {
    final List<Map<String, dynamic>> result = [];
    final headingRegex = RegExp(r'\*\*(.*?)\*\*\n([\s\S]*?)(?=\n\*\*|\n?$)');
    final subpointRegex = RegExp(r'^\s*[-*]\s*(.+)', multiLine: true);

    final headingMatches = headingRegex.allMatches(text);
    for (var match in headingMatches) {
      String heading = match.group(1)?.trim() ?? "";
      String content = match.group(2)?.trim() ?? "";
      List<String> subpoints = [];

      for (var subMatch in subpointRegex.allMatches(content)) {
        subpoints.add(subMatch.group(1)?.trim() ?? "");
      }

      result.add({
        'heading': heading,
        'subpoints': subpoints,
      });
    }
    return result;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black, // Set background color to black for a dark theme
      body: SingleChildScrollView(
        child: Center(
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                SizedBox(height: 40),

                // Image display
                if (_image != null)
                  ClipRRect(
                    borderRadius: BorderRadius.circular(12),
                    child: Image.file(
                      _image!,
                      width: 300,
                      height: 300,
                      fit: BoxFit.cover,
                    ),
                  )
                else
                  Text(
                    'No image selected',
                    style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
                  ),

                SizedBox(height: 20),

                // Buttons
                ElevatedButton(
                  onPressed: _pickImage,
                  child: Text('Pick an Image'),
                ),
                SizedBox(height: 10),
                ElevatedButton(
                  onPressed: _image == null ? null : () => _sendImageToServer(_image!),
                  child: Text('Submit'),
                ),

                SizedBox(height: 30),

                // Server response
                if (_responseText.isNotEmpty)
                  Text(
                    _responseText,
                    style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
                    textAlign: TextAlign.center,
                  ),

                if (_isLoading)
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: CircularProgressIndicator(),
                  ),

                // Cure and Prevention Box
                if (_preventionList.isNotEmpty)
                  Container(
                    width: double.infinity,
                    margin: EdgeInsets.only(top: 20),
                    padding: EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.8),
                      borderRadius: BorderRadius.circular(10),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.grey.shade400,
                          blurRadius: 8,
                          spreadRadius: 1,
                          offset: Offset(0, 3),
                        ),
                      ],
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: _preventionList.map((entry) {
                        return Padding(
                          padding: const EdgeInsets.only(bottom: 12.0),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              // Heading
                              Text(
                                entry['heading'],
                                style: TextStyle(
                                  fontSize: 18,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.green.shade800,
                                ),
                              ),
                              SizedBox(height: 6),

                              // Subpoints
                              ...entry['subpoints'].map<Widget>((point) {
                                return Padding(
                                  padding: const EdgeInsets.only(left: 8.0, bottom: 4.0),
                                  child: Row(
                                    crossAxisAlignment: CrossAxisAlignment.start,
                                    children: [
                                      Text(
                                        "• ",
                                        style: TextStyle(fontSize: 16, color: Colors.black87),
                                      ),
                                      Expanded(
                                        child: Text(
                                          point,
                                          style: TextStyle(fontSize: 14, color: Colors.black87),
                                        ),
                                      ),
                                    ],
                                  ),
                                );
                              }).toList(),
                            ],
                          ),
                        );
                      }).toList(),
                    ),
                  ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
