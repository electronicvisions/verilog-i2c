from waflib.extras.test_base import summary


def depends(ctx):
    pass


def options(opt):
    opt.load("pytest")


def configure(cfg):
    cfg.load("python")
    cfg.check_python_version((3,))
    cfg.load("pytest")


def build(bld):
    bld(name="verilog_i2c_tests",
        features="pytest",
        tests=bld.path.ant_glob("tb/test_*.py"),
        # Test scripts make assumptions about relative paths to sources
        path=bld.path.find_node('tb'),
        test_timeout=240)

    bld.add_post_fun(summary)
