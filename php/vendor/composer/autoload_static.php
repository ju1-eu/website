<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit9ef9a191e6dc8ea42df6111a96c67c14
{
    public static $prefixesPsr0 = array (
        'P' => 
        array (
            'Parsedown' => 
            array (
                0 => __DIR__ . '/..' . '/erusev/parsedown',
            ),
        ),
    );

    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixesPsr0 = ComposerStaticInit9ef9a191e6dc8ea42df6111a96c67c14::$prefixesPsr0;
            $loader->classMap = ComposerStaticInit9ef9a191e6dc8ea42df6111a96c67c14::$classMap;

        }, null, ClassLoader::class);
    }
}