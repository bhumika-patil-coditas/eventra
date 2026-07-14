package com.example.auth_service.dtos.Request;

import lombok.Data;

@Data
public class OtpVerifyRequest {
    private String email;
    private String code;
}
