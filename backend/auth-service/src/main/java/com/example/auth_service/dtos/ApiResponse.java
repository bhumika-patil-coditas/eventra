package com.example.auth_service.dtos;

import lombok.Data;
import org.springframework.web.ErrorResponse;

import java.time.LocalDateTime;
import java.util.List;

@Data
public class ApiResponse<T> {
    private boolean success;
    private String message;
    private T data;
    private LocalDateTime timestamp;

    public ApiResponse(boolean success, String message, T data, LocalDateTime timestamp) {
        this.success = success;
        this.message = message;
        this.data = data;
        this.timestamp = timestamp;
    }

    private List<ErrorResponse> errorResponseList;

    public ApiResponse(List<ErrorResponse> errorResponseList) {
        this.errorResponseList = errorResponseList;
    }
}
