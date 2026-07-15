package com.example.auth_service.controller;

import com.example.auth_service.Service.AuthService;
import com.example.auth_service.dtos.Request.OtpRequest;
import com.example.auth_service.dtos.Request.OtpVerifyRequest;
import com.example.auth_service.dtos.Response.AuthResponse;
import com.example.auth_service.dtos.Response.OtpResponse;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@RequestMapping("/auth/api/v1/otp")
public class AuthController {

    private final AuthService authService;

    @PostMapping("/request-otp")
    public ResponseEntity<OtpResponse> requestOtp(@RequestBody @Valid OtpRequest request) {
        return ResponseEntity.ok(authService.generateAndSendOtp(request.getEmail()));
    }

    @PostMapping("/verify-otp")
    public ResponseEntity<AuthResponse> verifyOtp(@RequestBody @Valid OtpVerifyRequest request) {
        String token = authService.verifyOtpAndIssueToken(request.getEmail(), request.getCode());
        return ResponseEntity.ok(new AuthResponse(token));
    }
}
