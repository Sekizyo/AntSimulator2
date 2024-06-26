from modules.engine import Engine

def test_fps():
    engine = Engine(testRun=True)
    avgFps = engine.run()

    assert avgFps > 50


def test_logic():
    engine = Engine(testRun=True)
    engine.fps = 100
    engine.grid.addFood((1, 11))
    engine.grid.addAntNest((780, 780))
    for _ in range(100):
        engine.grid.addAnts((780, 798))
    
    avgFps = engine.run()


    assert avgFps > 100
