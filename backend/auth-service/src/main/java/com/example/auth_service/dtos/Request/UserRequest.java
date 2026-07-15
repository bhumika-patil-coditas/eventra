package com.example.auth_service.dtos.Request;

import com.example.auth_service.constants.Role;
import lombok.Data;

@Data
public class UserRequest {
    private  String name;
    private  String email;
    private Role role;
}
