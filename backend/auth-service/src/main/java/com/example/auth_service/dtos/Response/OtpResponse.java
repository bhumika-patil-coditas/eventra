package com.example.auth_service.dtos.Response;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class OtpResponse {
    private String otp;
    private String expiration_in_milliSeconds;
}
