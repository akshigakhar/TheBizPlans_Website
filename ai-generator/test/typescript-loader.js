import { readFile } from 'node:fs/promises';
import { transformWithOxc } from 'vite';

export async function load(url, context, nextLoad) {
  if (!url.endsWith('.ts')) {
    return nextLoad(url, context);
  }

  const source = await readFile(new URL(url), 'utf8');
  const result = await transformWithOxc(source, new URL(url).pathname, {
    lang: 'ts',
    sourcemap: true,
  });

  return {
    format: 'module',
    shortCircuit: true,
    source: result.code,
  };
}
