cmake_minimum_required(VERSION 3.5)
project(shapes)

# Define o padrão C++
set(CMAKE_CXX_STANDARD 11)

set(sources shapes.cpp shapesDTO.cpp shapesFactory.h)

add_executable(MAIN main.cpp ${sources})

target_include_directories(MAIN PRIVATE ${PROJECT_SOURCE_DIR})
