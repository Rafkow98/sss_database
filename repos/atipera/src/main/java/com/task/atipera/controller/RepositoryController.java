package com.task.atipera.controller;

import com.task.atipera.dto.repository.RepositoryDTO;
import com.task.atipera.exception.UserNotFoundException;
import com.task.atipera.service.RepositoryService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

import java.util.*;

import static org.springframework.http.HttpStatus.NOT_FOUND;

@RestController
@Tag(name = "Github Repositories By User")
public class RepositoryController {
    private RepositoryService repositoryService;

    private ModelMapper mapper;

    @GetMapping("/{username}")
    @Operation(summary = "Get GitHub repositories for requested username")
    public List<RepositoryDTO> getReposFromUser(@PathVariable String username) {
        try {
            return mapAsList(repositoryService.getReposFromUser(username), RepositoryDTO.class);
        }
        catch (UserNotFoundException e) {
            throw new ResponseStatusException(NOT_FOUND, e.getMessage());
        }
    }

    protected <S, D> List<D> mapAsList(Collection<S> collection, Class<D> targetClass) {
        return collection.stream()
                .map(i -> mapper.map(i, targetClass))
                .toList();
    }

    @Autowired
    public void setRepositoryService(RepositoryService repositoryService) {
        this.repositoryService = repositoryService;
    }

    @Autowired
    public void setMapper(ModelMapper mapper) {
        this.mapper = mapper;
    }
}
