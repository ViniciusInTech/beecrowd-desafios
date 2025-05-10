cmake_minimum_required(VERSION 3.31)
project(beecrowd_desafios C)

set(CMAKE_C_STANDARD 99)

# Busca todos os arquivos main.c nas subpastas
file(GLOB_RECURSE SOURCE_FILES c/*/main.c)

foreach(file ${SOURCE_FILES})
    # Extrai o nome do diretório para usar como nome do executável
    get_filename_component(dir ${file} DIRECTORY)
    get_filename_component(name ${dir} NAME)

    # Cria um executável para cada exercício
    add_executable(${name} ${file}
            c/1016_distance/main.c
            c/1017_fuel_spent/main.c)

    # Linka a biblioteca matemática
    target_link_libraries(${name} m)
endforeach()
