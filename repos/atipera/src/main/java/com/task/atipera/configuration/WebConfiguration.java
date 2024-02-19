package com.task.atipera.configuration;

import com.task.atipera.converter.branch.BranchConverter;
import com.task.atipera.converter.repository.RepositoryConverter;
import com.task.github.client.GithubClient;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.*;
import org.springframework.format.FormatterRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfiguration implements WebMvcConfigurer {

    private BranchConverter branchConverter;
    private RepositoryConverter repositoryConverter;

    @Override
    public void addFormatters(FormatterRegistry registry) {
        registry.addConverter(branchConverter);
        registry.addConverter(repositoryConverter);
    }

    @Bean
    public ModelMapper modelMapper() {
        return new ModelMapper();
    }

    @Bean
    public GithubClient githubClient(@Value("${api.github.url}") String url) {
        return new GithubClient(url);
    }

    @Bean
    public OpenAPI garageOpenAPI() {
        return new OpenAPI()
                .info(new Info().title("GitHub repositories API")
                        .description("API for accessing GitHub repositories information")
                        .version("v0.0.1"));
    }

    @Autowired
    public void setBranchConverter(final BranchConverter branchConverter) {
        this.branchConverter = branchConverter;
    }

    @Autowired
    public void setRepositoryConverter(final RepositoryConverter repositoryConverter) {
        this.repositoryConverter = repositoryConverter;
    }
}
