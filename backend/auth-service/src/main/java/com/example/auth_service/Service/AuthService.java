package com.example.auth_service.Service;

import com.example.auth_service.dtos.Response.OtpResponse;
import com.example.auth_service.entities.User;
import com.example.auth_service.exception.InvalidOtpException;
import com.example.auth_service.exception.NotFoundException;
import com.example.auth_service.repository.UserRepository;
import com.example.auth_service.util.JwtUtil;
import lombok.RequiredArgsConstructor;
import org.apache.coyote.BadRequestException;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.Random;

@Service
@RequiredArgsConstructor
public class AuthService {
    private final UserRepository userRepository;
    private final RedisService redisService;
    private final JwtUtil jwtUtil;

    public OtpResponse generateAndSendOtp(String email) {
        User user = userRepository.findByEmail(email)
                .orElseThrow(() ->  new NotFoundException("User not found"));
        String code = String.valueOf(new Random().nextInt(900000) + 100000);
        redisService.saveOtp(user.getEmail(), code);
        return new OtpResponse(code,"900000");
    }

    public String verifyOtpAndIssueToken(String email, String code) {
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new NotFoundException("User not Found"));

        String otp = redisService.getOtp(user.getEmail());
        System.out.println("otp: " + otp);
        if(!otp.equals(code)) {
            throw new InvalidOtpException("Invalid OTP");
        }
        return jwtUtil.generateToken(user);
    }
}
