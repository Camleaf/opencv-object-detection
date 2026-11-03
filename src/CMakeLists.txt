add_subdirectory(implementation)
target_include_directories(implementation PUBLIC header)

find_package(OPENCV CONFIG REQUIRED)

add_executable(objdect main.cpp)

include_directories(object PRIVATE ${OPENCV_INCLUDE_DIRS})

target_link_libraries(objdect PRIVATE ${OPENCV_LIBRARIES})
target_link_libraries(objdect PRIVATE implementation)
