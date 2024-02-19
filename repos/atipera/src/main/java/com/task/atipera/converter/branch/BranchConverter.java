package com.task.atipera.converter.branch;


import com.task.atipera.converter.BaseConverter;
import com.task.atipera.data.branch.Branch;
import com.task.github.client.data.branch.BranchData;
import org.springframework.core.convert.converter.Converter;
import org.springframework.stereotype.Component;

@Component
public class BranchConverter extends BaseConverter implements Converter<BranchData, Branch> {
    @Override
    public Branch convert(BranchData source) {
        Branch target = new Branch();

        target.setName(source.getName());
        target.setLastCommitSha(source.getCommit().getSha());

        return target;
    }
}
