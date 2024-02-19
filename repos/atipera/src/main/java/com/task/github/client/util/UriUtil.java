package com.task.github.client.util;

public class UriUtil {

    public static String removeOptionalParametersFromUri(String uri) {
        uri = removeOptionalParametersFromUri(uri, "?");
        return removeOptionalParametersFromUri(uri, "/");
    }

    private static String removeOptionalParametersFromUri(String uri, final String optionalParameterMarker) {
        for (int firstIndex = uri.indexOf("{" + optionalParameterMarker); firstIndex != -1; firstIndex = uri.indexOf("{" + optionalParameterMarker)) { // while loop
            int lastIndex = uri.indexOf('}', firstIndex);
            uri = uri.substring(0, firstIndex) + uri.substring(lastIndex + 1);
        }
        return uri;
    }
}
