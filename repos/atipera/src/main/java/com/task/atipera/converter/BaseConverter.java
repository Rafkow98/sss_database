package com.task.atipera.converter;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.core.convert.ConversionService;
import org.springframework.stereotype.Component;

@Component
public class BaseConverter {

    private ConversionService conversionService;
    private ApplicationContext applicationContext;

    public ConversionService getConversionService() {
        if(conversionService == null) {
            conversionService = applicationContext.getBeansOfType(ConversionService.class).values().stream().findFirst().orElseThrow();
        }
        return conversionService;
    }

    @Autowired
    public void setApplicationContext(final ApplicationContext applicationContext) {
        this.applicationContext = applicationContext;
    }
}
