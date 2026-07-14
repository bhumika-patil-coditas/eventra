package com.example.auth_service.controller;

import com.example.auth_service.Service.UserService;
import com.example.auth_service.dtos.Request.UserRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/v1/user")
@CrossOrigin(origins = "http://localhost:8080/")
public class UserController {

    private final UserService userService;

    @PostMapping
    public ResponseEntity<String> registerUser(@RequestBody UserRequest userRequest) {
        return ResponseEntity.ok(userService.registerUser(userRequest));
    }

    @GetMapping("/me")
    public ResponseEntity<String> getUser() {
        return ResponseEntity.ok("Hello Bhoomika");
    }
}
