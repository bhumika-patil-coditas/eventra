package com.example.auth_service.dtos.Request;

import jakarta.validation.constraints.NotBlank;
import lombok.Data;

@Data
public class OtpRequest {

    @NotBlank(message = "Email can't be null")
    private String email;
}
