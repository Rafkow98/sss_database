package com.task.atipera.handler;

import com.task.atipera.response.ApiErrorResponse;

import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.server.ResponseStatusException;

@ControllerAdvice
public class ApiExceptionHandler {

    @ExceptionHandler({ResponseStatusException.class})
    public ResponseEntity<ApiErrorResponse> handleNoHandlerFoundException(final ResponseStatusException e) {
        ApiErrorResponse apiErrorResponse = new ApiErrorResponse(404, e.getReason());
        return ResponseEntity.status(HttpStatus.NOT_FOUND).contentType(MediaType.APPLICATION_JSON).body(apiErrorResponse);
    }
}
