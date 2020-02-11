RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

run_compose () {
  docker-compose -f $1 up --build --exit-code-from $2
  if [ $? -ne 0 ] ; then
    printf "${RED} $3 ${NC}\n"
    exit -1
  fi
}

run_compose docker-compose-tests.yml scraper_test "ERROR: Tests failed."
run_compose docker-compose.yml scraper "ERROR: Capturing data from the website failed."
printf "${GREEN} Tests and capturing data successful. ${NC}\n"