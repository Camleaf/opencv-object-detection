cmake_minimum_required(VERSION 3.25)

set(project_name "opencv-object-detection")

# project definition
project(${project_name} 
    VERSION 0.0.2 
    LANGUAGES CXX
)


# c++ settings
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)



set(BUILD_ENVIRONMENT "$ENV{BUILD_ENVIRON}") # set to Production when doing production builds
add_definitions(-DBUILD_ENVIRONMENT="${BUILD_ENVIRONMENT}")
message(INFO ": Building for ${BUILD_ENVIRONMENT}")

# for intellisense
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# for output
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/../bin/)

file(REMOVE_RECURSE ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}) # clear directory for new files to be built


include("${CMAKE_SOURCE_DIR}/vcpkg/scripts/buildsystems/vcpkg.cmake")


# add parts
add_subdirectory(src)
