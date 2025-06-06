cmake_minimum_required(VERSION 3.8)
project(misora2_launch_uoa)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

find_package(misora2_distribute_image)
find_package(misora2_qr)
find_package(misora2_pressure)
find_package(misora2_cracks)
find_package(misora2_metal_loss)

install(
  DIRECTORY launch
   DESTINATION share/${PROJECT_NAME}/
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
