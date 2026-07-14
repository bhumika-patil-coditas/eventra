package com.example.auth_service.Service;

import com.example.auth_service.dtos.Request.UserRequest;
import com.example.auth_service.entities.User;
import com.example.auth_service.exception.AlreadyExistsException;
import com.example.auth_service.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class UserService {
    private final UserRepository userRepository;

    @Transactional
    public String registerUser(UserRequest request) {
        if(userRepository.existsByEmail(request.getEmail())) {
            throw new AlreadyExistsException("User already exists");
        }
        User user = User.builder()
                .email(request.getEmail())
                .role(request.getRole())
                .name(request.getName())
                .isActive(true).build();
        userRepository.save(user);
        return user.getEmail()+" user added successfully";
    }
}
