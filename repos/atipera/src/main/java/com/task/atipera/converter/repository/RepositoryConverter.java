package com.task.atipera.converter.repository;

import com.task.atipera.converter.BaseConverter;
import com.task.atipera.data.branch.Branch;
import com.task.atipera.data.repository.Repository;
import com.task.github.client.data.repository.RepositoryData;
import org.springframework.core.convert.converter.Converter;
import org.springframework.stereotype.Component;

@Component
public class RepositoryConverter extends BaseConverter implements Converter<RepositoryData, Repository> {
    @Override
    public Repository convert(RepositoryData source) {
        Repository target = new Repository();

        target.setName(source.getName());
        target.setOwner(source.getOwner().getLogin());
        target.setBranches(source.getBranches().stream().map(b -> getConversionService().convert(b, Branch.class)).toList());

        return target;
    }
}
