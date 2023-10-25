# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "C:/Espressif/frameworks/esp-idf-v5.0.4/components/bootloader/subproject"
  "C:/Users/rdgbr/Documents/University-Stuff/Fall-2023/Capstone-2/ESP-DL/model_deployment/build/bootloader"
  "C:/Users/rdgbr/Documents/University-Stuff/Fall-2023/Capstone-2/ESP-DL/model_deployment/build/bootloader-prefix"
  "C:/Users/rdgbr/Documents/University-Stuff/Fall-2023/Capstone-2/ESP-DL/model_deployment/build/bootloader-prefix/tmp"
  "C:/Users/rdgbr/Documents/University-Stuff/Fall-2023/Capstone-2/ESP-DL/model_deployment/build/bootloader-prefix/src/bootloader-stamp"
  "C:/Users/rdgbr/Documents/University-Stuff/Fall-2023/Capstone-2/ESP-DL/model_deployment/build/bootloader-prefix/src"
  "C:/Users/rdgbr/Documents/University-Stuff/Fall-2023/Capstone-2/ESP-DL/model_deployment/build/bootloader-prefix/src/bootloader-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Users/rdgbr/Documents/University-Stuff/Fall-2023/Capstone-2/ESP-DL/model_deployment/build/bootloader-prefix/src/bootloader-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/Users/rdgbr/Documents/University-Stuff/Fall-2023/Capstone-2/ESP-DL/model_deployment/build/bootloader-prefix/src/bootloader-stamp${cfgdir}") # cfgdir has leading slash
endif()
