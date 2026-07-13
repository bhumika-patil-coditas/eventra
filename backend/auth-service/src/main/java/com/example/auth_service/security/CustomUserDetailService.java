package com.example.auth_service.security;

import com.example.auth_service.entities.User;
import com.example.auth_service.exception.NotFoundException;
import com.example.auth_service.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class CustomUserDetailService implements UserDetailsService {

    private final UserRepository userRepository;

    public User loadUserByUsername(String username) throws NotFoundException {
        return userRepository.findByEmail(username).orElseThrow(
                () -> new NotFoundException("Not Found"));
    }
}
