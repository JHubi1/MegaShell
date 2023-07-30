from files.internal import info as inf
from files.internal import constants as const
import os

const.constant("VERSION", inf.VERSION)
const.constant(["WORKING_DIR"], os.getcwd())