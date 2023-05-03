def test(test_name='', default_params={}, multi=False):
    def decorator(test_func):
        default_params['multi'] = multi
        test_obj = TEST(test_name, test_func, default_params)
        TEST_SUITE.add_test(test_obj)
        return test_obj

    return decorator