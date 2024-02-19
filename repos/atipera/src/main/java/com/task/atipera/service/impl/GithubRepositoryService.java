package com.task.atipera.service.impl;

import com.task.atipera.data.repository.Repository;
import com.task.atipera.exception.UserNotFoundException;
import com.task.atipera.service.RepositoryService;
import com.task.github.client.GithubClient;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.convert.ConversionService;
import org.springframework.stereotype.Service;
import org.springframework.web.client.HttpClientErrorException;

import java.util.List;

@Service
public class GithubRepositoryService implements RepositoryService {
    private GithubClient githubClient;

    private ConversionService conversionService;

    @Override
    public List<Repository> getReposFromUser(String username) {
        try {
            return githubClient.getReposFromUser(username).stream()
                    .filter(r -> !r.getFork())
                    .peek(r -> r.setBranches(githubClient.getBranchesFromRepo(r)))
                    .map(r -> conversionService.convert(r, Repository.class))
                    .toList();
        }
        catch (HttpClientErrorException.NotFound e) {
            throw new UserNotFoundException("Username does not belong to a github user", e);
        }
    }

    @Autowired
    public void setGithubClient(GithubClient githubClient) {
        this.githubClient = githubClient;
    }

    @Autowired
    public void setConversionService(ConversionService conversionService) {
        this.conversionService = conversionService;
    }
}