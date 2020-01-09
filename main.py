import rabbitListener as rl
import database as db
import loggerHelper

def main():
    loggerHelper.setupLogger()
    db.connect()
    rl.connect()

main()
