# genpy

The Python ROS message and service generator.

## Examples for generating messages with dependencies

```console
./scripts/genmsg_py.py -p std_msgs -Istd_msgs:`rospack find std_msgs`/msg -o gen `rospack find std_msgs`/msg/String.msg
./scripts/genmsg_py.py -p geometry_msgs -Istd_msgs:`rospack find std_msgs`/msg -Igeometry_msgs:`rospack find geometry_msgs`/msg -o gen `rospack find geometry_msgs`/msg/PoseStamped.msg
```

## Running Tests
1. Make and activate a virtual environment: `python -m venv env && source env/bin/activate`
2. Install requirements: `pip install -r requirements.txt`
3. Install genpy: `pip install -e ./`
4. Build test messages: `python ./test/msg/generate_test_messages.py`
5. Run pytest: `pytest`